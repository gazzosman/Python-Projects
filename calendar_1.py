from pathlib import Path

try:
    from google.auth.transport.requests import Request  # type: ignore[import-not-found]
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Google Calendar dependencies are not installed. Run: "
        "python -m pip install google-auth google-auth-oauthlib "
        "google-api-python-client"
    ) from exc

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    credentials_file = script_dir / "credentials.json"
    token_file = script_dir / "token.json"

    creds = None
    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not credentials_file.exists():
                raise FileNotFoundError(
                    f"Google OAuth credentials file not found: {credentials_file}"
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_file), SCOPES
            )
            creds = flow.run_local_server(port=0)

        token_file.write_text(creds.to_json(), encoding="utf-8")

    service = build("calendar", "v3", credentials=creds)
    page_token = None
    while True:
        calendar_list = (
            service.calendarList().list(pageToken=page_token).execute()
        )
        for calendar in calendar_list.get("items", []):
            print(calendar["summary"])
        page_token = calendar_list.get("nextPageToken")
        if not page_token:
            break


if __name__ == "__main__":
    main()
