<Button label="Link" variant="link" />
<Button as="a" label="External" href="https://vuejs.org/" target="_blank" rel="noopener" />
<Button asChild v-slot="slotProps">
    <RouterLink to="/" :class="slotProps.class">Router</RouterLink>
</Button>