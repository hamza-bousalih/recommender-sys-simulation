from torch import nn
import torch
import os
import kagglehub


class RecommenderModel:
    model_path_file = 'model_path.txt'
    kaggle_model = 'bousalihhamza/rs-user-item/PyTorch/default/1'

    def __init__(self, embedding_dim=32):
        self.num_users = 583964
        self.num_items = 546895
        self.embedding_dim = embedding_dim
        self.model = self._initialize_model()
        self._load_model()

    def _initialize_model(self):
        class DeepCollaborativeFiltering_target(nn.Module):
            def __init__(self, num_users, num_items, embedding_dim=32):
                super(DeepCollaborativeFiltering_target, self).__init__()
                self.user_embedding = nn.Embedding(num_users, embedding_dim)
                self.item_embedding = nn.Embedding(num_items, embedding_dim)
                self.fc1 = nn.Linear(embedding_dim * 2, 128)
                self.fc2 = nn.Linear(128, 64)
                self.output = nn.Linear(64, 1)

            def forward(self, user_ids, item_ids):
                user_emb = self.user_embedding(user_ids)
                item_emb = self.item_embedding(item_ids)
                x = torch.cat([user_emb, item_emb], dim=1)
                x = torch.relu(self.fc1(x))
                x = torch.relu(self.fc2(x))
                x = torch.sigmoid(self.output(x))
                return x

        return DeepCollaborativeFiltering_target(self.num_users, self.num_items, self.embedding_dim)

    def _load_model_path(self):
        if os.path.exists(self.model_path_file):
            with open(self.model_path_file, 'r') as f:
                return f.read().strip()
        return None

    def _save_model_path(self, path):
        with open(self.model_path_file, 'w') as f:
            f.write(path)

    def _load_model(self):
        model_path = self._load_model_path()
        if not model_path:
            model_path = kagglehub.model_download(self.kaggle_model, path='model.pth', force_download=True)
            self._save_model_path(model_path)
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu'), weights_only=True))
        self.model.eval()
    
    def recommend(self, user_id: int, items: list, k: int):
        probabilities = []
        with torch.no_grad():
            for item_id in items:
                user_tensor = torch.tensor([user_id], dtype=torch.long)
                item_tensor = torch.tensor([item_id], dtype=torch.long)
                probability = self.model(user_tensor, item_tensor).item()
                probabilities.append((item_id, probability))
        probabilities = sorted(probabilities, key=lambda x: -x[1])
        return probabilities[:k]
