module.exports = {
  apps: [
    {
      name: "adjial",
      script: "npm start",
    },
  ],
  deploy: {
    production: {
      user: "root",
      host: "155.133.22.183",
      repo: "git@github.com:AmineDr/adjial-website.git",
      ref: "origin/master",
      key: "key.pem",
      path: "/home/ci-cd/adjial",
      "pre-deploy-local": "",
      "post-deploy": "source ~/.nvm/nvm.sh && npm install && npm run build && systemctl restart nginx.service && pm2 reload ecosystem.config.js --env production",
      "pre-setup": "",
      "ssh_options": "ForwardAgent=yes",
    },
  },
};
