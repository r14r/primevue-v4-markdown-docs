<Timeline :value="events">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>