<ToggleSwitch v-model="checked">
    <template #handle="{ checked }">
        <i :class="['!text-xs pi', { 'pi-check': checked, 'pi-times': !checked }]" />
    </template>
</ToggleSwitch>