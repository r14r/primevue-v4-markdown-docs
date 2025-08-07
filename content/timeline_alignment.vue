<Timeline :value="events" class="w-full md:w-80">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>

<Timeline :value="events" align="right" class="w-full md:w-80">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>

<Timeline :value="events" align="alternate" class="w-full md:w-80">
    <template #content="slotProps">
        {{ slotProps.item.status }}
    </template>
</Timeline>