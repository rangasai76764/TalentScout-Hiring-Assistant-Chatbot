import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional


class DataHandler:
    def __init__(self, file_path: Optional[str] = None):
        """
        Initialize handler with optional custom file path.
        Defaults to 'candidate_data.json'.
        """
        self.FILE_PATH = Path(file_path) if file_path else Path("candidate_data.json")

        try:
            if self.FILE_PATH.exists():
                with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            else:
                self.data = []
                # Ensure file is created on init
                with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                    json.dump(self.data, f)
        except Exception:
            self.data = []

    def save(
        self,
        candidate_info: dict,
        sentiment: Optional[str] = None,
        language: Optional[str] = None,
        personalization: Optional[dict] = None,
    ):
        """
        Save candidate info after anonymizing sensitive fields.
        Email and phone are hashed with SHA256.
        Also stores sentiment, language, and personalization details.
        """
        info_copy = candidate_info.copy()

        # Hash sensitive fields
        if "email" in info_copy and info_copy["email"]:
            info_copy["email"] = self._hash(info_copy["email"])
        if "phone" in info_copy and info_copy["phone"]:
            info_copy["phone"] = self._hash(info_copy["phone"])

        # Add metadata
        info_copy["saved_at"] = datetime.utcnow().isoformat()
        if sentiment:
            info_copy["sentiment"] = sentiment
        if language:
            info_copy["language"] = language
        if personalization:
            info_copy["personalization"] = personalization

        self.data.append(info_copy)

        # Persist to disk
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
            f.flush()

    def export_anonymized_json(self) -> str:
        """Return a string representation of anonymized JSON for downloads."""
        return json.dumps(self.data, indent=2, ensure_ascii=False)

    def clear_all(self):
        """Remove all stored records (useful for privacy/purging)."""
        self.data = []
        try:
            if self.FILE_PATH.exists():
                self.FILE_PATH.unlink()
        except Exception:
            pass

    def _hash(self, value: str) -> str:
        return hashlib.sha256(str(value).encode("utf-8")).hexdigest()
