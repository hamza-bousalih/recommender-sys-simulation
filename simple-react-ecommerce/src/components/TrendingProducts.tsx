import { useAppSelector } from "../redux/hooks";
import ProductList from "./ProductList";

const TrendingProducts = () => {
  const featuredProducts = useAppSelector(
    (state) => state.productReducer.featuredProducts
  );
  const username = useAppSelector((state) => state.authReducer.username);

  return <ProductList title={username == ""? "Random Products": "Products For You"} products={featuredProducts} />;
};

export default TrendingProducts;
