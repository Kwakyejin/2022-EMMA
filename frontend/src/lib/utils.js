export async function get(uri) {
  let url = "http://10.125.218.100:9025";
  const response = await fetch(url + uri);
  return await response.json();
}
