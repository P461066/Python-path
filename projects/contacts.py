def contact_nexus():
    # Master nested dictionary container
    contact_book = {}
    
    while True:
        print("\n" + "="*35)
        print("    ⚡ THE TERMINAL CONTACT NEXUS")
        print("="*35)
        print("1. ➕ Add New Contact")
        print("2. 📇 View All Contacts")
        print("3. 🔍 Search Contact")
        print("4. 🔌 Exit Nexus")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            print("\n--- ADD NEW CONTACT ---")
            name = input("Enter contact name: ").strip().title()
            
            if not name:
                print("⚠️ Error: Name cannot be blank!")
                continue
                
            phone = input(f"Enter phone number for {name}: ").strip()
            email = input(f"Enter email for {name}: ").strip()
            fax   = input(f"Enter fax number for {name} (retro mode): ").strip()
            
            # Store using nested dictionary assignment (creates or overwrites)
            contact_book[name] = {
                "phone": phone if phone else "N/A",
                "email": email if email else "N/A",
                "fax":   fax if fax else "N/A"
            }
            print(f"✅ Success: {name} saved to the Nexus!")
            
        elif choice == '2':
            if not contact_book:
                print("\n⚠️ Nexus database is currently empty.")
            else:
                print("\n--- DIRECTORY MANIFEST ---")
                for name, details in contact_book.items():
                    print(f"👤 {name}")
                    print(f"   ├── Phone: {details['phone']}")
                    print(f"   ├── Email: {details['email']}")
                    print(f"   └── Fax:   {details['fax']}")
                    
        elif choice == '3':
            if not contact_book:
                print("\n⚠️ Nexus database is empty. Nothing to search.")
                continue
                
            search_term = input("\nEnter name to search: ").strip().title()
            found = False
            
            print(f"\n--- SEARCH RESULTS FOR '{search_term}' ---")
            for name, details in contact_book.items():
                # Check if search term matches part of the name
                if search_term in name:
                    print(f"🎯 Match Found:")
                    print(f"👤 {name}")
                    print(f"   ├── Phone: {details['phone']}")
                    print(f"   ├── Email: {details['email']}")
                    print(f"   └── Fax:   {details['fax']}")
                    found = True
                    
            if not found:
                print(f"❌ No records found matching '{search_term}'.")
                
        elif choice == '4':
            print("\n🔌 Disconnecting from Nexus. System shutting down. Goodbye!")
            break
            
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    contact_nexus()