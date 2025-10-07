<template>
  <div>
    <div class="mt-1 flex items-center justify-center gap-1 p-1 rounded-lg bg-neutral-dark border border-neutral-medium">
      <NuxtLink v-for="section in sections" :key="section.id" :to="section.link"
              :class="['px-1 py-1.5 rounded-md text-sm font-medium transition-colors',
                       isActive(section.link) ? 'bg-secondary text-neutral-lightest' : 'text-neutral-light hover:bg-neutral-medium']">
        {{ section.title }}
      </NuxtLink>
    </div>

    <button @click="navigate(-1)"
            class="fixed left-4 top-1/2 -translate-y-1/2 p-2 rounded-full bg-neutral-dark hover:bg-secondary z-10 transition-all">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-neutral-lightest" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" /></svg>
    </button>
    <button @click="navigate(1)"
            class="fixed right-4 top-1/2 -translate-y-1/2 p-2 rounded-full bg-neutral-dark hover:bg-secondary z-10 transition-all">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-neutral-lightest" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7" /></svg>
    </button>
    
    <div class="w-full max-w-4xl mx-auto">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const props = defineProps({
  sections: {
    type: Array,
    required: true
  }
});

const route = useRoute();
const router = useRouter();

const currentSectionIndex = computed(() => {
  return props.sections.findIndex(section => section.link === route.path);
});

const isActive = (link) => {
  return route.path === link;
};

const navigate = (direction) => {
  const currentIndex = currentSectionIndex.value;
  let newIndex = (currentIndex + direction + props.sections.length) % props.sections.length;
  router.push(props.sections[newIndex].link);
};
</script>