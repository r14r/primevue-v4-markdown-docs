<ConfirmPopup group="templating">
    <template #message="slotProps">
        <div class="flex flex-col items-center w-full gap-4 border-b border-surface-200 dark:border-surface-700 p-4 mb-4 pb-0">
            <i :class="slotProps.message.icon" class="!text-6xl text-primary-500"></i>
            <p>{{ slotProps.message.message }}</p>
        </div>
    </template>
</ConfirmPopup>
<Button @click="showTemplate($event)" label="Save"></Button>