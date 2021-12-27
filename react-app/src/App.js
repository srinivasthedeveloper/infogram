import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Uploader from "./components/Uploader";
import Home from "./screens/Home";
import React, { useState, useEffect, useCallback } from "react";
import Sidebar from "./components/Sidebar";
import axios from "axios";
import debounce from "lodash.debounce";

// import ImageUpload from "./screens/ImageUpload";

function App() {
  const [isUploaderOpen, setUploaderOpen] = useState(false);
  const handleUploader = (e) => {
    setUploaderOpen(e);
  };
  const [data, setData] = useState([]);

  const debouncedFunction = useCallback(
    debounce((e) => updateToggle(e), 500),
    []
  );

  const updateToggle = (e) => {
    try {
      const response = axios.put(
        `http://127.0.0.1:8000/post/${e[2]}`,
        { ...e[1] },
        {
          headers: { "Content-Type": "application/json" },
        }
      );
      console.log("response:-", response);
    } catch (error) {
      console.log(error);
    }
  };
  const handleToogle = (e) => {
    let update = [...data];
    update[e[0]] = { ...update[e[0]], ...e[1] };
    setData(update);
    debouncedFunction(e);
  };

  const handleComment = (e) => {
    let update = [...data];
    update[e[0]]["comment"].push(e[1]);
    setData(update);
  };

  const updatePost = async (id, post) => {
    try {
      console.log("update data:- ", id, JSON.stringify(post));
      const res = await axios.put(
        `http://127.0.0.1:8000/posts/${id}/update`,
        { body: JSON.stringify(post) },
        { headers: { "Content-Type": "application/json" } }
      );
      console.log("response:- ", res);
    } catch (error) {
      console.log("error:- ", error);
    }
  };

  const getApiData = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/posts");
      console.log("response is:- ", JSON.stringify(res.data));
      setData(res.data);
    } catch (e) {
      console.log("the_error", e);
    }
  };

  useEffect(() => {
    getApiData();
  }, []);

  return (
    <div className="app">
      {/* <ImageUpload /> */}
      <Header />
      <div style={{ display: "grid", placeItems: "center" }}>
        <div style={{ display: "flex", alignItems: "flex-start" }}>
          <div className="appHome">
            <Home
              data={data}
              handleToogle={handleToogle}
              handleComment={handleComment}
            />
          </div>
          <Sidebar username="SrinivasTheDeveloper" logo={"image.jpg"} />
        </div>
        <Uploader isOpen={isUploaderOpen} handleClose={handleUploader} />
      </div>
      <Footer
        username="SrinivasTheDeveloper"
        logo={"image.jpg"}
        isUploaderOpen={isUploaderOpen}
        handleUploader={handleUploader}
      />
    </div>
  );
}

export default App;
