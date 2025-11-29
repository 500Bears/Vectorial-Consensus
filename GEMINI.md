# Project: AI Mind Palace: A Visualization of Vectorial Consensus

## Directory Overview

This directory contains the source code for an interactive, 3D web-based visualization called "AI Mind Palace: A Visualization of Vectorial Consensus." The project aims to provide an intuitive and engaging explanation of the internal workings of a Large Language Model (LLM), from input to "thought" (Vectorial Consensus) to grounded output.

## Key Files

-   **`index.html`**: The main entry point of the application, containing all the HTML structure, CSS styling, and JavaScript logic for the 3D visualization and user interaction.
-   **`README.md`**: Provides a comprehensive introduction to the project, its features, the core concept of "Vectorial Consensus," and a detailed explanation of the AI's internal architecture as visualized.
-   **`TODO.md`**: Outlines the development roadmap, detailing planned features and their implementation phases.
-   **`LICENSE`**: Specifies the licensing information for the project (MIT License).
-   **`.gitignore`**: Standard Git ignore file to exclude unnecessary files from version control.

## Project Type

This is a **client-side web application** focused on interactive data visualization.

## Technology Stack

*   **Frontend:** HTML5, CSS3, JavaScript
*   **3D Graphics:** Three.js
*   **API Integration:** Gemini API (for text generation and Text-to-Speech capabilities)

## Building and Running

The project is a pure frontend application and does not require any complex build steps.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/500bears/Vectorial-Consensus.git
    cd Vectorial-Consensus
    ```
2.  **Open `index.html`:**
    Simply open the `index.html` file in a modern web browser (e.g., Chrome, Firefox, Edge).

The application will load directly in your browser. If no Gemini API key is provided, it will automatically start in "Demo Mode."

## Development Conventions

*   **Single-Page Application:** The entire application logic (HTML, CSS, JavaScript) is contained within `index.html` for simplicity.
*   **Phased Development:** Features are tracked and planned using the `TODO.md` file.
*   **Conceptual Documentation:** The `README.md` serves as a primary source for understanding the theoretical underpinnings and components of the visualization.
*   **"Bring Your Own Key" (BYOK) Feature:** Users can optionally provide their own Gemini API key via a settings modal to enable live queries, with the key stored locally in `localStorage`.

## Current Development Focus

The current development focus, as indicated by the `TODO.md` and recent interactions, is on implementing the "Bring Your Own Key" (BYOK) feature to allow users to switch between a demo mode and live API interaction. This involves:

*   Adding a settings icon and modal for API key input.
*   Storing the API key securely in `localStorage`.
*   Dynamically enabling/disabling live query functionality based on the presence of an API key.
