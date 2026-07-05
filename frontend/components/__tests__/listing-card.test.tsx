import { render, screen } from "@testing-library/react";
import { ListingCard } from "../listing-card";
import { fallbackListings } from "@/lib/api";

describe("ListingCard", () => {
  it("renders listing title and price", () => {
    render(<ListingCard listing={fallbackListings[0]} />);
    expect(screen.getByText(fallbackListings[0].title)).toBeInTheDocument();
    expect(screen.getByText(`$${fallbackListings[0].price}`)).toBeInTheDocument();
  });
});
