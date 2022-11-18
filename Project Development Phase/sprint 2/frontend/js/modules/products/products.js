import { constants } from "../../constants.js";

const productsWrapper = document.querySelector("#products");
const loader = document.querySelector("#loader");
const token = localStorage.getItem("token");
const requestHeaders = {
  headers: {
    Authorization: 'Bearer ' + token
  }
};

window.addEventListener('load', () => {
  loader.classList.remove('d-none');
  getProducts();
});

const getProducts = async () => {
  try {
    const { data } = await axios.get(
      `${constants.BASE_URL}/products/all`,
      requestHeaders
    );
    createProductCards(data.data);
  }
  catch (err) {
    console.error("Get Products Error: ", error);
  }
  finally {
    loader.classList.add('d-none');
  }
}

const createProductCards = (products) => {
  products.map((product) => {
    productsWrapper.innerHTML +=
      `<div class="product" id='card-${product.id}'>
      <div class="product-header">
        <h4 class="product-name">${product.name}</h4>
        <div>
          <button class="action-btn edit-btn" data-id=${product.id}>
            <i class="fas fa-pen"></i>
          </button>
          <button class="action-btn delete-btn" data-id=${product.id}>
            <i class="fas fa-trash"></i>
          </button>
          <button class="action-btn save-edit-btn d-none" data-id=${product.id}>
            <i class="fas fa-check"></i>
          </button>
        </div>
      </div>
      <p class="product-des">${product.description}</p>
    </div>`;
  });
}