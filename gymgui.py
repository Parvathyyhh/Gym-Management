import streamlit as st
from gymView import GymMemberManager

member_instance=GymMemberManager()
plans=["1 month","2 months","3 months","6 months","8 months","1 year"]

tab1,tab2,tab3,tab4=st.tabs(["Add Member","View Member Details","Update Details","Delete Member"])
with tab1:
    st.header("Add New Member..!")
    name=st.text_input("Enter name")
    place=st.text_input("Enter place")
    mobile=st.text_input("Enter mobile number")
    plan=st.selectbox("Select Plan",["1 month","2 months","3 months","6 months","8 months","1 year"])
    fee=st.text_input("Enter fee")
    joined_date=st.date_input("Enter joined date")
    if st.button("Submit"):
        member_instance.post(name=name,place=place,mobile=mobile,plan=plan,fee=fee,joined_date=joined_date)
        st.success("Member Added Successfully..!")
with tab2:
    st.header("View Gym Member Details..!")
    records=member_instance.get()
    print("______________")
    print(records)
    if records:
        st.table(records)
    else:
        st.warning("No member found..!")
with tab3:
    st.title("Update Member Details")
    record=member_instance.get()
    if records:
        member_ids=[r[0] for r in records]
        id=st.selectbox("Select Member id",member_ids,key="update_id")
        record=member_instance.get_object(id=id)
        name=st.text_input("Enter name",value=record[1])
        place=st.text_input("Enter your place",value=record[2])
        mobile=st.text_input("Enter mobile number",value=record[3])
        plan=st.selectbox("Select your plan",plans,index=plans.index(record[4]))
        joined_date=st.date_input("Enter joined date",value=record[5])
    if st.button("Update"):
        status,message=member_instance.put(id=id,
                                           name=name,
                                           place=place,
                                           mobile=mobile,
                                           plan=plan,
                                           joined_date=joined_date)
        if status:
            st.success(message)
            st.rerun()
        else:
            st.error(message)
    else:
        st.warning("No member found..!")
