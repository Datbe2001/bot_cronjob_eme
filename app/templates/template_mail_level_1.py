def template_mail_lv_1(pending_event, pending_event_previous, this_shift):
    html_template = f"""
            <div>
              <div style="max-width: 800px; margin: auto">
                <p>Dear User by Level 1,</p>
                <p>
                  This is a reminder that you have {pending_event} pending events that need
                  to be completed in this shift ({this_shift}).
                </p>
                <p>📌 Pending Events Details:</p>
                <p>
                  Total Pending Events: {pending_event}
                  <br />
                  Pending from Previous: {pending_event_previous}
                  <br />
                  Due on This Shift: {this_shift}
                  <br />
                  🔗 Please complete these events before your shift ends:
                  <a href="https://emagiceyes.rainscales.com"
                    >https://emagiceyes.rainscales.com</a
                  >
                </p>
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
