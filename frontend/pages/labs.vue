<template>
  <div>
    <h2 :class="[theme.typography.h2, theme.typography.headings]">Labs</h2>
    <p :class="[theme.colors.neutral.light, 'mt-1', 'text-sm']">Manage lab orders and view results.</p>
    
    <MultiPanelNavigation :sections="sections" />

    <div class="mt-4">
      <NuxtPage />
    </div>
  </div>
</template>

<script setup>
import MultiPanelNavigation from '~/components/MultiPanelNavigation.vue';

definePageMeta({ layout: "default" });

const theme = useTheme();

const sections = [
  { id: 'orders', title: 'Orders', link: '/labs' },
  { id: 'results', title: 'Results', link: '/labs/results' },
  { id: 'new', title: 'New Order', link: '/labs/new' },
];
</script>