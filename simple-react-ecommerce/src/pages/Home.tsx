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
      fetch("http://127.0.0.1:5000/items?userid=1&count=30")
        .then((res) => res.json())
        .then(({ products }) => {
          const productList: Product[] = [];
          products.forEach((product: Product) => {
            productList.push({
              id: product.id,
              title: product.title,
              images: product.images,
              price: product.price,
              rating: product.rating,
              thumbnail: product.thumbnail,
              description: product.description,
              category: product.category,
              discountPercentage: product.discountPercentage,
            });
          });
          dispatch(updateFeaturedList(productList.slice(0, 10)));
          dispatch(updateNewList(productList.slice(10, 30)));
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
