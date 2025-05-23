# 🔍 Legal Lens – Chrome Extension for T&C Summarization

**Legal Lens** is a Chrome extension designed to simplify the complex language of Terms & Conditions. It helps users quickly understand what they’re agreeing to by providing clear, concise summaries using a basic self-built NLP model.

---

## 📌 What It Does

- 📃 Extracts and analyzes website terms and conditions.
- 🧠 Uses a lightweight, custom NLP model to generate short, user-friendly summaries.
- ⚖️ Highlights important legal points like data usage, user rights, and hidden clauses.

---

## 🛠️ Built With

- **HTML, CSS, JavaScript** – Frontend for the extension interface.
- **Basic NLP model (Python)** – Trained for summarization of legal language.
- **Flask (Optional)** – To serve the NLP model if needed.
- **Chrome Extension APIs** – For integrating with browser content.

---

## 🚀 Getting Started

To use locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/Nivedanbelwal/CYBER_SECURITY_PBL_TEAM_DETECTIVES.git
   cd CYBER_SECURITY_PBL_TEAM_DETECTIVES

   *****structure for files*****

├── icons/             # Extension icons
├── content.js         # Extracts T&C text from web pages
├── popup.html         # User interface of the extension
├── popup.js           # Displays summary from the NLP model
├── manifest.json      # Chrome extension metadata
├── styles.css         # Styling for the popup
└── nlp_model/         # Directory for your basic NLP code

👥 Team
Nivedan Belwal,
Vyomesh Chauhan,
Sourabh Kumar Singh,
Vansh Pant


