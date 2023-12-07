import { StrictMode } from "react";
import ReactDOM from "react-dom";
import App from "./App";
import Store from "global-context-store";

// We'll use <Helmet /> to link to an external stylesheet
// for the @blueprintjs/icons peer dependency. We also import
// additional base styles here:
import { Helmet } from "react-helmet";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <Helmet>
      <link href="https://unpkg.com/label-studio@latest/build/static/css/main.css" rel="stylesheet" />
    </Helmet>

    <Store>
      <App />
    </Store>
  </StrictMode>,
  rootElement
);
