<script setup>
definePageMeta({
  layout: "default",
})
const theme = useTheme()
</script>

<template>
  <div>
    <h2 :class="[theme.sectionTitle, theme.colors.primary]">Patients</h2>
    <p :class="theme.colors.muted">Manage patient demographics & insurance records.</p>

    <div :class="[theme.card, theme.colors.bgCard, theme.colors.border, 'mt-6']">
      🚧 Coming soon: Patient list & profile view
    </div>
  </div>
</template>
