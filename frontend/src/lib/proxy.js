const { createProxyMiddleware } = require("http-proxy-middleware");

const proxy = createProxyMiddleware({
  target: "http://10.125.218.100:5177", // Replace with your API server URL
  changeOrigin: true,
});

module.exports = function (app) {
  app.use("../routes", proxy); // Specify the route where the proxy should be applied
};
