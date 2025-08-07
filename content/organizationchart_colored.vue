<OrganizationChart :value="data" collapsible>
    <template #person="slotProps">
        <div class="flex flex-col">
            <div class="flex flex-col items-center">
                <img :alt="slotProps.node.data.name" :src="slotProps.node.data.image" class="mb-4 w-12 h-12" />
                <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                <span>{{ slotProps.node.data.title }}</span>
            </div>
        </div>
    </template>
    <template #default="slotProps">
        <span>{{ slotProps.node.label }}</span>
    </template>
</OrganizationChart>