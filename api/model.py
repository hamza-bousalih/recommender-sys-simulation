from torch import nn
import torch

class DeepCollaborativeFiltering_target(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim=32):
        super(DeepCollaborativeFiltering_target, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        self.fc1 = nn.Linear(embedding_dim * 2, 128)
        self.fc2 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 1)  # Sortie unique pour binaire

    def forward(self, user_ids, item_ids):
        user_emb = self.user_embedding(user_ids)
        item_emb = self.item_embedding(item_ids)
        x = torch.cat([user_emb, item_emb], dim=1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.output(x))  # Activation sigmoïde pour classification binaire
        return x

#---------------------------------------------------
num_users_target = 583964
num_items_target = 546895 

model = DeepCollaborativeFiltering_target(num_users_target, num_items_target)
model.load_state_dict(torch.load("./model.pth"))
model.eval()
#---------------------------------------------------

def recommande(user_id: int, items: list, k: int):
    probabilities = []
    
    with torch.no_grad():
        for item_id in items:
            user_tensor = torch.tensor([user_id], dtype=torch.long)
            item_tensor = torch.tensor([item_id], dtype=torch.long)

            probability = model(user_tensor, item_tensor).item()
            probabilities.append((item_id, probability))

    probabilities = sorted(probabilities, key=lambda x: -x[1])

    return probabilities[:k]
