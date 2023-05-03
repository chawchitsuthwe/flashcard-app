import { BrowserRouter, Routes, Route } from "react-router-dom";
import CategoryList from "./Components/Category/CategoryList";
import Header from "./Components/Common/Header";
import Container from "react-bootstrap/esm/Container";

function App() {
  return (
    <BrowserRouter>
      <div>
        <Header></Header>
        <Container className="my-3">
          <Routes>
            <Route element={<CategoryList />} path="/" />
          </Routes>
        </Container>
      </div>
    </BrowserRouter>
  );
}

export default App;
