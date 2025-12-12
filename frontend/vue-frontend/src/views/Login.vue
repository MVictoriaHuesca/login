<template>
  <div class="center-screen">
    <h1>Bienvenido</h1>
    <p>Inicia sesión para continuar</p>
    
    <a href="https://app-git-main-victorias-projects-f2384d75.vercel.app/auth/login/google" class="btn-google">
      Ingresar con Google
    </a>
  </div>
</template>

<style scoped>
.center-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.btn-google {
  background-color: #4285F4;
  color: white;
  padding: 12px 24px;
  text-decoration: none;
  border-radius: 4px;
  font-family: sans-serif;
  font-weight: bold;
}
.btn-google:hover {
  background-color: #357ae8;
}
</style>