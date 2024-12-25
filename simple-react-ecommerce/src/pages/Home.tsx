import { FC, useEffect } from "react";
import HeroSection from "../components/HeroSection";
import ForYouProducts from "../components/TrendingProducts";
import { Product } from "../models/Product";
import {
  updateFeaturedList,
  updateNewList,
} from "../redux/features/productSlice";
import { useAppDispatch } from "../redux/hooks";

const Home: FC = () => {
  const dispatch = useAppDispatch();

  useEffect(() => {
    const fetchProducts = () => {
      fetch("https://dummyjson.com/products?limit=24")
        .then((res) => res.json())
        .then(({ products }) => {
          const productList: Product[] = [];
          products.forEach((product: Product) => {
            productList.push({
              id: product.id,
              title: `Title ${product.id}`,
              images: product.images,
              price: Math.round(Math.random() * 100),
              rating: Math.round(Math.random() * 5),
              thumbnail: product.thumbnail,
              description: `Description ${product.id}`,
              category: `Category ${product.id}`,
              discountPercentage: Math.round(Math.random() * 50),
            });
          });
          dispatch(updateFeaturedList(productList.slice(0, 8)));
          dispatch(updateNewList(productList.slice(8, 16)));
        });
    };
    fetchProducts();
  }, [dispatch]);

  return (
    <div className="dark:bg-slate-800">
      <HeroSection />
      {/* <Features /> */}
      <ForYouProducts />
      {/* <Banner /> */}
      {/* <Testimonials /> */}
      <br />
    </div>
  );
};

export default Home;
