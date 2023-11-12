import React, { useState } from "react";
import LabelStudio from "label-studio";
import './styles.css';

const backend = "http://localhost";
const nextImageEndpoint = `${backend}/next-image`;
const saveAnswerEndpoint = `${backend}/save-answer`;
const imagesFolder = `${backend}/static/images`;

export default function App() {
  const [currentImage, setCurrentImage] = useState("");
  React.useEffect(() => {
    const username = extractUsername()
    fetch(`${nextImageEndpoint}/${username}`)
      .then((response) => response.text())
      .then((path) => {
        setCurrentImage(path);
      });
  }, []);

  if (currentImage === "") {
    return <div style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      height: "100vh",
      fontWeight: "bold",
    }}>Loading...</div>;
  }

  if (currentImage === "No more images!") {
    return (<div style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      height: "100vh",
      fontWeight: "bold",
    }}>No more images!</div>);
  }

  return (<LabelStudioTest currentImage={currentImage} />);
}



function LabelStudioTest({ currentImage }) {
  const [selected, setSelected] = useState(false);

  React.useEffect(() => {
    new LabelStudio("label-studio", {
      config: `
      <View>
          <Image name="image1" value="$image"/>
          
          <Choices name="choice" toName="image1" showInLine="true">
              <Choice value="Real" background="blue"/>
              <Choice value="Fake" background="green" />
          </Choices>
          
          <Header value="If you think the image is fake press the following button to mark the part of the image that you think is fake:" />
          <BrushLabels name="tag" toName="image1">
              <Label value="Mark" background="rgba(0, 0, 255, 0.5)"/>
          </BrushLabels>
          
          <Header value="Describe why you think it's fake (press enter when done):" />
          <TextArea name="answer" maxSubmissions="10" editable="true" required="false" />
      </View>
      `,

      interfaces: [
        "submit",
        "skip",
        "controls",
      ],

      task: {
        annotations: [],
        predictions: [],
        id: 1,
        data: {
          image: `${imagesFolder}/${currentImage}`,
        }
      },

      onLabelStudioLoad: function (LS) {
        var c = LS.annotationStore.addAnnotation({
          userGenerate: true
        });
        LS.annotationStore.selectAnnotation(c.id);
      },
      onSubmitAnnotation: function (LS, annotation) {
        const requestBody = JSON.stringify({ "answer": JSON.stringify(annotation.serializeAnnotation()) });
        console.log(requestBody);
        fetch(`${saveAnswerEndpoint}/${extractUsername()}/${currentImage}`, {
          method: "POST",
          cache: "no-cache",
          headers: {
            "Content-Type": "application/json",
          },
          referrerPolicy: "no-referrer",
          body: requestBody,
        }).then((response) => {
          window.location.reload();
        });
      },
      onUpdateAnnotation: function (LS, annotation) {
        window.location.reload();
      },
      onSkipTask: function (LS) {
        console.log("Skip task");
        window.location.reload();
      },
    });
  }, []);

  return (
    <div
      id="label-studio"
      style={{
        margin: "auto",
        width: "800px",
      }}
    ></div>
  );
}

function extractUsername() {
  var url = new URL(window.location.href);
  var username = url.searchParams.get("username");
  return username;
}

