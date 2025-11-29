### Phase 1: Core Functionality & UX (Current Focus)

*   [x] ~~Implement stable base visualization.~~
*   [x] ~~Add interactive "Demo Mode" for API-less experience.~~
*   [ ] **Implement "Bring Your Own Key" (BYOK) Panel:**
    *   [ ] Add a settings icon (⚙️).
    *   [ ] Create a modal for API key input.
    *   [ ] Use `localStorage` to save the key securely in the user's browser.
    *   [ ] Unlock live queries and text input when a key is present.

### Phase 2: Multi-API & Multi-Modal Expansion

*   [ ] **API Abstraction Layer:**
    *   [ ] Refactor the API call logic to support multiple providers.
    *   [ ] Add a dropdown in the settings panel to select an API provider (Gemini, OpenAI, Grok, etc.).
*   [ ] **Multi-Modal Generation:**
    *   [ ] **Image Generation:** Add a new "Visualize" button that sends the concept to an image generation model and displays the result.
    *   [ ] **Audio Generation:** Explore more advanced TTS features or sound generation.
    *   [ ] **Video/Document:** Scope and design how to represent these modalities.

### Phase 3: UI/UX "Pleasure to Use" Polish

*   [ ] **Floating Token Labels:** Visualize subwords during the tokenization phase.
*   [ ] **Dynamic Head Tooltips:** Add "echo trails" and hover-info for attention beams.
*   [ ] **Post-Collapse "Echo":** Create a visual effect showing the output returning to the memory banks.
*   [ ] **Embeddable Essay:** Create a slide-in "Lore Panel" with the V-Consensus text.
