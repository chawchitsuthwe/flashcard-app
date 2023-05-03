import React, { useEffect, useState } from "react";
import Table from "react-bootstrap/Table";
import Button from 'react-bootstrap/Button';
import { getCategories } from "../../Services/CategoryService";

const CategoryList = (props) => {
  const [categories, setCategories] = useState([]);

  useEffect(()=> {
    getCategories().then((res) => {
      setCategories(res.data)
    });
  }, []);

  return (
    <div>
      <h2>Categories</h2>
      <Table bordered hover>
        <thead>
          <tr>
            <th>No</th>
            <th>Name</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {
            categories.map(
              (category, idx) => (
                <tr key={ idx + 1 }>
                  <td>{ idx + 1 }</td>
                  <td>{ category.name }</td>
                  <td>
                    <Button variant="primary">Update</Button>{' '}
                    <Button variant="danger">Delete</Button>
                  </td>
                </tr>
              )
            )
          }
        </tbody>
      </Table>
    </div>
  );
};

export default CategoryList;
