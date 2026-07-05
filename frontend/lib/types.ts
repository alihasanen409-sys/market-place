export type Listing = {
  id: string;
  title: string;
  slug: string;
  short_description: string;
  description: string;
  price: string;
  status: string;
  product_type: string;
  rating_avg: string;
  sales_count: number;
  images: { image_url: string; alt_text: string; is_primary: boolean }[];
};

export type Category = {
  id: string;
  name: string;
  slug: string;
  description: string;
};

export type ApiPage<T> = {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
};
