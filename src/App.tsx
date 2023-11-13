import { useState } from "react";
import "./App.css";
import apiClient from "./api/client";

interface RandomData {
  some: string;
  something_else: string;
}
function App() {
  const [randomData, setRandomData] = useState<RandomData | null>(null);

  const getData = () => {
    apiClient
      .get("/data")
      .then((r) => {
        const response = r.data;
        console.log(response);

        setRandomData({
          some: response.some,
          something_else: response.more,
        });
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <>
      <p>To see some random info:</p>
      <button onClick={getData}>Click Me!</button>
      {randomData && (
        <div>
          <p>some: {randomData.some}</p>
          <p>more: {randomData.something_else}</p>
        </div>
      )}
    </>
  );
}

export default App;
