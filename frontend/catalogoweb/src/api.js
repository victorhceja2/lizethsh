export const fetchProductos = async () => {
  const res = await fetch('http://127.0.0.1:8000/productos/');
  const data = await res.json();
  return data;
};
