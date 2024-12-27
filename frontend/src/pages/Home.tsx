import { FC, useEffect } from "react";
import HeroSection from "../components/HeroSection";
import ForYouProducts from "../components/TrendingProducts";
import { Product } from "../models/Product";
import {
  updateFeaturedList,
  updateNewList,
} from "../redux/features/productSlice";
import { useAppDispatch, useAppSelector } from "../redux/hooks";

const Home: FC = () => {
  const dispatch = useAppDispatch();
  const id = useAppSelector((state) => state.authReducer.id);
  

  useEffect(() => {
    const fetchProducts = () => {
      fetch(`http://127.0.0.1:5000/products?userid=${id}&count=30`)
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
              probability: product.probability ? Math.floor((product.probability ?? 0) * 10000) / 10000: undefined,
            });
          });
          productList.sort((a, b) => (b.probability ?? 0) - (a.probability ?? 0));
          dispatch(updateFeaturedList(productList.slice(0, 10)));
          dispatch(updateNewList(productList.slice(10, 30)));
        });
    };
    fetchProducts();
  }, [dispatch, id]);

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
