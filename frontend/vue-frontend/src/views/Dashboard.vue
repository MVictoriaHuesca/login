<template>
  <div v-if="user">
    <h1>Hola, {{ user.username }}!</h1>
    <p>Tu email es: {{ user.email }}</p>
    
    <button @click="logout">Cerrar Sesión</button>
  </div>
  <div v-else>
    Cargando datos del usuario...
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../services/api'; // Usamos nuestra instancia configurada
import { useRouter } from 'vue-router';

const user = ref(null);
const router = useRouter();

onMounted(async () => {
  try {
    // Hacemos petición a ruta protegida de FastAPI
    const response = await api.get('/users/me');
    user.value = response.data;
  } catch (error) {
    console.error("Error al obtener usuario", error);
    // Si el token es inválido o expiró, sacar al usuario
    logout();
  }
});

const logout = () => {
  // 1. Borrar token
  localStorage.removeItem('token');
  // 2. Redirigir al Login
  router.push('/');
};
</script>