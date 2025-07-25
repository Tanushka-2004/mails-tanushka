from mail_utils import send_email
import json
import os

password = os.environ.get("EMAIL_PASSWORD")
attachment_paths = [os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'attachments', 'Brochure.pdf')
)]

total_time = 0
count = 0

filepath = os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'data', 'internal_team.json')
)

with open(filepath, 'r') as list:
  recipients = json.load(list)

for recipient in recipients:
  try:
    subject = "Collaboration Opportunity - TEDxPVGCOET X ASMITA ORGANIC FARMS"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{subject}</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">

      <!-- Top Banner (TEDxPVGCOET style) -->
      <div style="background-color: #000; color: white; padding: 20px 30px; border-bottom: 4px solid #e62b1e;">
        <div style="font-size: 28px; font-weight: bold;">
          <span style="color: #e62b1e;">TED</span><span style="color: white;">x</span>PVGCOET
        </div>
        <div style="font-size: 12px; color: #ccc; margin-top: 4px;">
          x = independently organized TED event
        </div>
      </div>

      <!-- Main Content -->
      
        <p><strong>Dear [Brand Name] Team,</strong></p>

          <p>I hope this message finds you well.</br>
          I’m Aarya Rahul Gandhe, a final-year student at PVGCOET, reaching out on behalf of <strong>TEDxPVGCOET</strong>.</p>

          <p>TEDx talks have long been a wellspring of inspiration and knowledge, staying true to their core mission: <strong>“Ideas Worth Spreading.”</strong> These events foster community engagement and provide a platform for local voices and changemakers to share their insights.</p>

          <p>This year, our central theme is <strong>“Drishti”</strong> – a Sanskrit word meaning <strong>“Perspective.”</strong> It represents how one person’s vision can bring fresh insights and drive meaningful change. As India continues to evolve, we believe it's crucial to bring together diverse perspectives to help shape a more inclusive and insightful future.</p>

          <p>We are actively seeking partners to collaborate with us on this exciting journey. In return, we are pleased to offer your brand the following <strong>exclusive sponsorship benefits:</strong></p>

          <ul>
            <li><strong>Enhanced Brand Visibility:</strong> Prominent logo placement throughout the event.</li>
            <li><strong>Media Coverage:</strong> Access to pre- and post-event promotions across our digital platforms.</li>
            <li><strong>On-Site Brand Showcase:</strong> Booths, banners, and product visibility at the venue.</li>
            <li><strong>Logo Integration:</strong> Featured on tickets, badges, flyers, and other event collaterals.</li>
            <li><strong>Speaker Interaction:</strong> Opportunities to engage with our diverse and renowned speaker panel.</li>
            <li><strong>Brand Feature in Event Newsletter:</strong> Reach 1000+ engaged subscribers.</li>
            <li><strong>Post-Event Analytics:</strong> Receive audience insights and engagement metrics to measure ROI.</li>
            <li><strong>Sponsor Spotlight:</strong> Long-term or title sponsors will receive a dedicated feature on our website, telling your brand’s story.</li>
          </ul>

          <p>We’re confident that this partnership will be mutually rewarding. We would love the opportunity to present our vision to your team and explore ways we can work together.Please feel free to reach out to us at <a href="mailto:tedx@pvgcoet.ac.in"><strong>tedx@pvgcoet.ac.in</strong></a> or contact me directly at the details below.</p>

          <p>Kindly find our event brochure attached for more details.</p>

          <p>Warm regards,<br>
          <strong>TEDxPVGCOET</strong><br>
          Aarya Gandhe<br>
          Treasurer<br>
          📞 9860945719<br>
          📧 <a href="mailto:tedx@pvgcoet.ac.in">tedx@pvgcoet.ac.in</a>
          </p>


      <!-- Bottom Banner -->
      <div style="height: 10px; background: linear-gradient(to right, #e62b1e, #000, #e62b1e); margin-top: 20px;"></div>
    </body>
    </html>
    """
    print(f"Sending mail to {recipient['name']} ({recipient['email']})...")
    this_time = send_email(recipient["email"], subject, body, password, attachment_paths)
    if this_time > 0:
      count += 1
      total_time += this_time
  except Exception as e:
    print(f"Failed to send mail to {recipient}: {e}")

print("Total IDs in the list:", len(recipients))
print("Total mails sent:", count)
print(f"Total time taken: {total_time:.2f} seconds")
print(f"Average time taken per mail: {total_time / count} seconds")
