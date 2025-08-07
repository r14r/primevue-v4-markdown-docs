<OrganizationChart :value="data" collapsible>
    <template #country="slotProps">
        <div class="flex flex-col items-center">
            <img :alt="slotProps.node.label" src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png" :class="`w-2rem flag flag-${slotProps.node.data}`" />
            <div class="mt-4 font-medium text-lg">{{ slotProps.node.label }}</div>
        </div>
    </template>
    <template #default="slotProps">
        <span>{{slotProps.node.data.label}}</span>
    </template>
</OrganizationChart>