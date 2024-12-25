import { FC } from "react";

const HeroSection: FC = () => {
  return (
    <div className="bg-[#e3edf6] dark:bg-slate-600 font-lora">
      <div className="container px-4 grid md:grid-cols-2 py-8 mx-auto">
        <div className="flex items-center">
          <div className="max-w-[450px] space-y-4">
            <h2 className="text-black font-bold text-4xl md:text-5xl dark:text-white">
              Simulation for E-Commerce Recommander System
            </h2>
            <h3 className="text-2xl dark:text-white">
              Cross-Domain Approach with <span className="text-red-600">Transfer Learning</span>.
            </h3>
            {/*<Link
              to="/product/6"
              data-test="hero-btn"
              className="inline-block bg-white rounded-md px-6 py-3 hover:bg-blue-500 hover:text-white"
            >
              Shop Now
            </Link>*/}
          </div>
        </div>
        <div>
          <img src="/hero.png" alt="hero" className="ml-auto" />
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
