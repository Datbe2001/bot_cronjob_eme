def template_mail_lv_2_3(pending_event, pending_event_previous, this_shift):
    html_template = f"""
            <div>
              <div style="max-width: 800px; margin: auto">
                <p>Dear User,</p>
                <p>
                  This is your daily summary of pending events that require your review and
                  approval.
                </p>
                <p>📌 Pending Events Details:</p>
                <p>
                  Total Pending Events: {pending_event}
                  <br />
                  Pending for More Than 1 Day: {pending_event_previous}
                  <br />
                  Due Today: {this_shift}
                  <br />
                  🔗 Please review these events before the end of the day:
                  <a href="https://emagiceyes.rainscales.com"
                    >https://emagiceyes.rainscales.com</a
                  >
                </p>
                <p>Your prompt action helps keep the process running smoothly.</p>
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
