<ConfirmDialog group="templating">
    <template #message="slotProps">
        <div class="flex flex-col items-center w-full gap-4 border-b border-surface-200 dark:border-surface-700">
            <i :class="slotProps.message.icon" class="!text-6xl text-primary-500"></i>
            <p>{{ slotProps.message.message }}</p>
        </div>
    </template>
</ConfirmDialog>
<Button @click="showTemplate()" label="Save"></Button>