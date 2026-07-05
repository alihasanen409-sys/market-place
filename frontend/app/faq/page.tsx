import { InfoPage } from "@/components/info-page";

export default function FAQPage() {
  return (
    <InfoPage title="FAQ">
      <p><strong>Is payment real?</strong> Development checkout is simulated so no card is charged.</p>
      <p><strong>Can sellers upload files?</strong> Yes, backend endpoints validate files and send them to Cloudinary when credentials are configured.</p>
      <p><strong>Is Arabic supported?</strong> Yes, the layout supports English, Arabic, and RTL switching.</p>
    </InfoPage>
  );
}
