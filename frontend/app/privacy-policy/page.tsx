import { InfoPage } from "@/components/info-page";

export default function PrivacyPolicyPage() {
  return (
    <InfoPage title="Privacy Policy">
      <p>The application stores account, order, listing, message, and notification data needed to run the marketplace.</p>
      <p>Production deployments should configure HTTPS, trusted origins, secure cookies, and Cloudinary upload restrictions.</p>
    </InfoPage>
  );
}
