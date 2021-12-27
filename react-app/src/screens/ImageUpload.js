import axios from "axios";
import React, { useRef, useState } from "react";

export default function ImageUpload(props) {
  const [image, setImage] = useState();
  const [file, setFile] = useState();
  return (
    <div>
      <form
        style={styles.container}
        onSubmit={(e) => {
          e.preventDefault();
        }}
        multiple={true}
      >
        <input
          style={{ alignSelf: "center", padding: "10px" }}
          type="file"
          accept="image/png, image/jpeg"
          onChange={(e) => setImage(e.target.files[0])}
        />
        <input
          style={{ padding: "10px", margin: "10px 0" }}
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button
          onClick={() => {
            try {
              let form_data = new FormData();
              image && form_data.append("sample1", image, image.name);
              file && form_data.append("sample2", file, file.name);
              console.log(JSON.stringify(form_data));
              const response = axios.put(
                "http://127.0.0.1:8000/image/4",
                form_data,
                {
                  headers: {
                    "content-type": "multipart/form-data",
                  },
                }
              );
              console.log("response:-", JSON.stringify(response));
            } catch (e) {
              console.error("error:-", e);
            }
          }}
          style={{
            ...styles.buttons,
            ...{
              background: "#0095f6",
              color: "#fff",
            },
          }}
        >
          Post
        </button>
        <button
          style={{
            ...styles.buttons,
            ...{
              background: "#ed4956",
              color: "#fff",
              margin: "10px 0",
            },
          }}
        >
          Cancel
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    padding: "10px",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    background: "#ddd",
    minHeight: "500%",
    minWidth: "400px",
  },
  buttons: {
    padding: "10px",
    border: "none",
    fontSize: "16px",
    fontWeight: "bold",
    borderRadius: "5px",
  },
};
