import React, { useRef, useState } from "react";
import MyModal from "./MyModal";
import axios from "axios";

export default function Uploader({ isOpen, handleClose }) {
  const imageRef = useRef();
  const textRef = useRef();
  const areaRef = useRef();
  const [isInValid, setValid] = useState(false);

  const handleUpload = (e) => {
    try {
      let form_data = new FormData();
      // form_data.append("image", e.image, e.image.name);
      // form_data.append("location", e.location);
      // form_data.append("caption", e.caption);
      Object.keys(e).map((item) => {
        if (item === "image") {
          form_data.append(item, e[item], e[item].name);
          form_data.append("sample1", e[item], e[item].name);
          form_data.append("sample2", e[item], e[item].name);
        } else {
          form_data.append(item, e[item]);
        }
      });
      const response = axios.post("http://127.0.0.1:8000/posts", form_data, {
        headers: {
          "content-type": "multipart/form-data",
        },
      });
      console.log("response:-", JSON.stringify(response));
    } catch (error) {
      console.error("error:-", error);
    }
  };

  return (
    <MyModal handleClose={handleClose} isOpen={isOpen}>
      <form
        style={styles.container}
        onSubmit={(e) => {
          e.preventDefault();
          if (
            imageRef.current.value === "" ||
            textRef.current.value === "" ||
            areaRef.current.value === ""
          ) {
            alert("Fields can't be empty");
            setValid(true);
          } else {
            // setValid(false);
            // handleClose(false);
            handleUpload({
              username: "UserName2",
              logo: "",
              location: textRef.current.value,
              caption: areaRef.current.value,
              image: imageRef.current.files[0],
            });
          }
        }}
        multiple={true}
      >
        <input
          style={{ alignSelf: "center", padding: "10px" }}
          ref={imageRef}
          type="file"
          //   onChange={(e) => console.log(e.target.files[0])}
        />
        <input
          style={{ padding: "10px", margin: "10px 0" }}
          ref={textRef}
          type="text"
          placeholder="Enter Location"
          //   onChange={(e) => console.log(e.target.value)}
        />
        <textarea
          style={{ height: "100px", margin: "0 0 10px 0" }}
          ref={areaRef}
          placeholder="Enter Caption"
          //   onChange={(e) => console.log(e.target.value)}
        />
        <button
          type="submit"
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
          type="button"
          onClick={() => {
            setValid(false);
            handleClose(false);
          }}
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
        {isInValid && (
          <p
            style={{
              padding: "10px",
              textAlign: "center",
              color: "red",
              fontWeight: "bold",
              fontStyle: "italic",
            }}
          >
            Fields can't be empty
          </p>
        )}
      </form>
    </MyModal>
  );
}

const styles = {
  container: {
    padding: "10px",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    background: "#fff",
    width: "50%",
    height: "50%",
    minHeight: "400px",
    minWidth: "400px",
    maxWidth: "600px",
    maxHeight: "600px",
  },
  buttons: {
    padding: "10px",
    border: "none",
    fontSize: "16px",
    fontWeight: "bold",
    borderRadius: "5px",
  },
};
