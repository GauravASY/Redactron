regex_types = {
    "aadhar" : r"\d{4}\s\d{4}\s\d{4}",
    "pan" : r"[A-Z]{5}[0-9]{4}[A-Z]",
    "passport" : r"[A-Z]{2}[0-9]{7}",
    "email" : r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "phone" : r"\+?[0-9]{10}",
    "address" : r"\d+\s+\w+\s+\w+",
    "dob" : r"\d{2}/\d{2}/\d{4}",
    "IFSC" : r"[A-Z]{4}[0-9]{6}",
}