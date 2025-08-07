<Timeline :value="events">
    <template #opposite="slotProps">
        <small class="text-surface-500 dark:text-surface-400">{{slotProps.item.date}}</small>
    </template>
    <template #content="slotProps">
        {{slotProps.item.status}}
    </template>
</Timeline>