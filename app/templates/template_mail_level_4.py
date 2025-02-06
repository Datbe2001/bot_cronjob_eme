def template_mail_lv_4(pending_event, pending_event_previous, this_shift):
    html_template = f"""
            <div>
              <div style="max-width: 800px; margin: auto">
                <p>Dear User by Level 4,</p>
                <p>
                  Here is your weekly summary of pending events that require your review and
                  approval.
                </p>
                <p>📌 Pending Events Details:</p>
                <p>
                  Total Pending Events: {pending_event}
                  <br />
                  Pending for More Than 7 Days: {pending_event_previous}
                  <br />
                  Due This Week: {this_shift}
                  <br />
                  🔗 Please review and approve/reject these events:
                  <a href="https://emagiceyes.rainscales.com"
                    >https://emagiceyes.rainscales.com</a
                  >
                </p>
                <p>Your weekly review ensures smooth workflow and compliance.</p>
                <br />
                <p>
                  Best regards, <br />
                  eMagicEyes Platform
                </p>
                <img
                  src="https://rainscales.com/wp-content/uploads/2024/02/Rainscales-logo.png"
                  alt="logo"
                  width="200"
                  height="100"
                  style="object-fit: contain"
                />
              </div>
            </div>

            """
    return html_template
