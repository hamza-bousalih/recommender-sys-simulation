import { useAppSelector } from "../redux/hooks";
import ProductList from "./ProductList";

const TrendingProducts = () => {
  const featuredProducts = useAppSelector(
    (state) => state.productReducer.featuredProducts
  );
  const id = useAppSelector((state) => state.authReducer.id);

  return <ProductList title={id == ""? "Random Products": "Products For You"} products={featuredProducts} />;
};

export default TrendingProducts;
