<template>
  <div>
    <div class="mt-1 flex items-center justify-center gap-1 p-1 rounded-lg bg-neutral-dark border border-neutral-medium">
      <NuxtLink v-for="section in sections" :key="section.id" :to="section.link"
              :class="['px-4 py-1.5 rounded-md text-sm font-medium transition-colors',
                       isActive(section.link) ? 'bg-secondary text-neutral-lightest' : 'text-neutral-light hover:bg-neutral-medium']">
        {{ section.title }}
      </NuxtLink>
    </div>

    
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