module.exports = {
  apps: [
    {
      name: "nextjs-flask-template",
      script: "npm start",
    },
  ],
  deploy: {
    production: {
      user: "cicd_user",
      host: "Your server's IP",
      repo: "git@github.com:Username/Repo.git",
      ref: "origin/master",
      key: "key.pem", // SSH KEY
      path: "/var/www/ci-cd/nextjs-flask-template",
      "pre-deploy-local": "git add . && git commit -m 'Pushing to production' && git push origin master",
      "post-deploy": "source ~/.nvm/nvm.sh && npm install && npm run build && systemctl restart nginx.service && pm2 reload ecosystem.config.js --env production",// What ever you want to execute post-deploy
      "pre-setup": "",
      "ssh_options": "ForwardAgent=yes",
    },
  },
};
