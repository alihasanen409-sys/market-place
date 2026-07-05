/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    cpus: 2
  },
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "res.cloudinary.com" },
      { protocol: "https", hostname: "images.unsplash.com" }
    ]
  }
};

module.exports = nextConfig;
