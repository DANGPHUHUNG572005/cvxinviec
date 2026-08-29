import streamlit as st

# ============================================================
# CẤU HÌNH TRANG
# ============================================================

st.set_page_config(
    page_title="CV - Đặng Phú Hưng",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS - THIẾT KẾ GIAO DIỆN CV
# ============================================================

st.markdown("""
<style>

    /* ==============================
       TOÀN BỘ TRANG
    ============================== */

    .stApp {
        background: #eef1f5;
    }

    .main {
        background: #eef1f5;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Ẩn menu Streamlit */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* ==============================
       KHUNG CV
    ============================== */

    .cv {
        max-width: 1100px;
        margin: 30px auto;
        background: #ffffff;
        padding: 50px 60px;
        border-radius: 4px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.10);
    }

    /* ==============================
       HEADER
    ============================== */

    .name {
        font-size: 42px;
        font-weight: 800;
        color: #17365d;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }

    .position {
        font-size: 18px;
        font-weight: 700;
        color: #555555;
        margin-bottom: 22px;
        text-transform: uppercase;
    }

    .contact {
        font-size: 15px;
        line-height: 1.9;
        color: #333333;
    }

    .contact b {
        color: #17365d;
    }

    /* ==============================
       TIÊU ĐỀ CÁC PHẦN
    ============================== */

    .section {
        margin-top: 35px;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 21px;
        font-weight: 800;
        color: #17365d;
        text-transform: uppercase;
        border-bottom: 2px solid #17365d;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }

    /* ==============================
       NỘI DUNG
    ============================== */

    .text {
        font-size: 15px;
        line-height: 1.8;
        color: #333333;
        text-align: justify;
    }

    .date {
        font-size: 14px;
        font-weight: 700;
        color: #666666;
        margin-bottom: 5px;
    }

    .organization {
        font-size: 17px;
        font-weight: 800;
        color: #222222;
        margin-bottom: 5px;
    }

    .major {
        font-size: 15px;
        color: #444444;
        margin-bottom: 8px;
    }

    .role {
        font-size: 14px;
        font-weight: 800;
        color: #17365d;
        margin: 10px 0;
    }

    /* ==============================
       CHỨNG CHỈ
    ============================== */

    .certificate {
        background: #f4f6f8;
        border-left: 4px solid #17365d;
        padding: 15px 18px;
        margin-bottom: 12px;
        border-radius: 3px;
    }

    .certificate-year {
        font-size: 14px;
        font-weight: 700;
        color: #777777;
    }

    .certificate-name {
        font-size: 15px;
        font-weight: 800;
        color: #222222;
        margin-top: 3px;
    }

    /* ==============================
       KỸ NĂNG
    ============================== */

    .skill {
        margin-bottom: 18px;
    }

    .skill-name {
        font-size: 15px;
        font-weight: 800;
        color: #17365d;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    .skill-description {
        font-size: 14px;
        line-height: 1.7;
        color: #444444;
    }

    /* ==============================
       SỞ THÍCH
    ============================== */

    .hobby {
        background: #f4f6f8;
        padding: 12px 15px;
        border-radius: 4px;
        text-align: center;
        font-size: 14px;
        color: #333333;
        margin-bottom: 10px;
    }

    /* ==============================
       HOẠT ĐỘNG
    ============================== */

    .activity {
        margin-bottom: 12px;
        font-size: 14px;
        line-height: 1.7;
        color: #333333;
    }

    .activity::before {
        content: "•";
        color: #17365d;
        font-weight: bold;
        margin-right: 8px;
    }

    /* ==============================
       NÚT TẢI / IN
    ============================== */

    .button-area {
        text-align: center;
        margin: 20px 0;
    }

    /* ==============================
       RESPONSIVE
    ============================== */

    @media (max-width: 768px) {

        .cv {
            margin: 10px;
            padding: 25px 20px;
        }

        .name {
            font-size: 30px;
        }

        .position {
            font-size: 14px;
        }

    }

    /* ==============================
       PRINT
    ============================== */

    @media print {

        .stApp {
            background: white !important;
        }

        .cv {
            box-shadow: none;
            margin: 0;
            max-width: 100%;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"] {
            display: none !important;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# NÚT IN CV
# ============================================================

st.markdown("""
<div style="
    max-width:1100px;
    margin:auto;
    text-align:right;
    margin-bottom:10px;
">
</div>
""", unsafe_allow_html=True)


# ============================================================
# BẮT ĐẦU CV
# ============================================================

st.markdown('<div class="cv">', unsafe_allow_html=True)


# ============================================================
# HEADER - THÔNG TIN CÁ NHÂN
# ============================================================

st.markdown("""
<div class="name">
    Đặng Phú Hưng
</div>

<div class="position">
    Sinh viên năm 3 ngành Tài chính Ngân hàng
</div>
""", unsafe_allow_html=True)


# Thông tin cá nhân
col_left, col_right = st.columns(2)

with col_left:

    st.markdown("""
    <div class="contact">
        <b>Ngày sinh:</b> 05/07/2005<br>
        <b>Giới tính:</b> Nam<br>
        <b>Số điện thoại:</b> 0909116235<br>
        <b>Email:</b> phuhung5705@gmail.com
    </div>
    """, unsafe_allow_html=True)

with col_right:

    st.markdown("""
    <div class="contact">
        <b>Website:</b> Facebook<br>
        <b>Địa chỉ:</b> 80/21 Tô Vĩnh Diện,<br>
        Khu phố Tân Hòa, Phường Đông Hòa,<br>
        Thành phố Hồ Chí Minh
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MỤC TIÊU NGHỀ NGHIỆP
# ============================================================

st.markdown("""
<div class="section">
    <div class="section-title">
        Mục tiêu nghề nghiệp
    </div>

    <div class="text">
        Áp dụng kiến thức chuyên ngành Tài chính – Ngân hàng cùng kỹ năng
        Word, Excel và phân tích dữ liệu để hỗ trợ hiệu quả các nghiệp vụ
        ngân hàng. Không ngừng học hỏi quy trình nghiệp vụ, nâng cao kỹ năng
        chuyên môn và hướng tới trở thành nhân sự ngân hàng chuyên nghiệp,
        có giá trị lâu dài cho tổ chức.
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# HỌC VẤN
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Học vấn
    </div>

    <div class="date">
        09/2023 - nay
    </div>

    <div class="organization">
        TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH
    </div>

    <div class="major">
        Chuyên ngành: <b>Tài chính ngân hàng</b>
    </div>

    <div class="text">
        • Xếp loại: Khá<br>
        • Chứng chỉ: Kỹ năng Hành chính văn phòng,
        Kỹ năng làm chủ công việc
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CHỨNG CHỈ
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Chứng chỉ
    </div>

</div>
""", unsafe_allow_html=True)


cert_col1, cert_col2 = st.columns(2)

with cert_col1:

    st.markdown("""
    <div class="certificate">

        <div class="certificate-year">
            2025
        </div>

        <div class="certificate-name">
            KỸ NĂNG HÀNH CHÍNH VĂN PHÒNG
        </div>

    </div>
    """, unsafe_allow_html=True)


with cert_col2:

    st.markdown("""
    <div class="certificate">

        <div class="certificate-year">
            2025
        </div>

        <div class="certificate-name">
            KỸ NĂNG LÀM CHỦ CÔNG VIỆC
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# KỸ NĂNG
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Kỹ năng
    </div>

</div>
""", unsafe_allow_html=True)


skills = [
    (
        "SOẠN THẢO VĂN BẢN",
        "Kỹ năng soạn thảo văn bản hành chính và học thuật. "
        "Thành thạo Microsoft Word, trình bày văn bản chuyên nghiệp. "
        "Kỹ năng viết và chỉnh sửa báo cáo."
    ),

    (
        "KỸ NĂNG BÀN PHÍM",
        "Kỹ năng bàn phím tốt, gõ nhanh và chính xác, "
        "sử dụng thành thạo phím tắt trong Word và Excel."
    ),

    (
        "GIẢI QUYẾT VẤN ĐỀ",
        "Phân tích tình huống, xác định nguyên nhân, "
        "đề xuất và lựa chọn giải pháp phù hợp."
    ),

    (
        "QUẢN LÍ THỜI GIAN",
        "Sắp xếp công việc theo mức độ ưu tiên, đảm bảo hoàn thành "
        "đúng hạn, cân bằng học tập và công việc."
    )
]


for skill_name, skill_description in skills:

    st.markdown(
        f"""
        <div class="skill">

            <div class="skill-name">
                {skill_name}
            </div>

            <div class="skill-description">
                {skill_description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SỞ THÍCH
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Sở thích
    </div>

</div>
""", unsafe_allow_html=True)


hobby1, hobby2, hobby3, hobby4 = st.columns(4)

with hobby1:
    st.markdown(
        '<div class="hobby">📚 Đọc sách</div>',
        unsafe_allow_html=True
    )

with hobby2:
    st.markdown(
        '<div class="hobby">🎧 Nghe podcast học tập</div>',
        unsafe_allow_html=True
    )

with hobby3:
    st.markdown(
        '<div class="hobby">🎓 Tham gia hoạt động học thuật</div>',
        unsafe_allow_html=True
    )

with hobby4:
    st.markdown(
        '<div class="hobby">💡 Tự học kỹ năng mềm</div>',
        unsafe_allow_html=True
    )


# ============================================================
# HOẠT ĐỘNG
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Hoạt động
    </div>

</div>
""", unsafe_allow_html=True)


# --------------------------
# HOẠT ĐỘNG NĂM 2024
# --------------------------

st.markdown("""
<div class="date">
    11/05/2024 - 23/12/2024
</div>

<div class="organization">
    TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH
</div>

<div class="role">
    SINH VIÊN THAM GIA
</div>
""", unsafe_allow_html=True)


activities_2024 = [
    "Tham gia UNITOUR nhà lãnh đạo tương lai và giới thiệu cuộc thi ASEAN - CHINA - INDIA 2024",
    "Tham gia Ngày hội tuyển dụng tháng 5 năm 2024",
    "Tham gia Workshop Đầu tư chứng khoán Bản lĩnh đầu tư & tự tin chiến thắng",
    "Tham gia Chương trình Tìm hiểu tài nguyên giáo dục mở cho Tân SV khoá 2024"
]

for activity in activities_2024:

    st.markdown(
        f'<div class="activity">{activity}</div>',
        unsafe_allow_html=True
    )


# --------------------------
# HOẠT ĐỘNG NĂM 2025
# --------------------------

st.markdown("""
<br>

<div class="date">
    09/08/2025 - 05/10/2025
</div>

<div class="organization">
    TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH
</div>

<div class="role">
    SINH VIÊN THAM GIA
</div>
""", unsafe_allow_html=True)


activities_2025 = [
    "Tham gia Hội thảo khoa học Quốc tế Toán học và Ứng dụng năm 2025",
    "Tham gia Hoạt động phục vụ cộng đồng cấp Khoa 2025 - Hành trình tuổi trẻ vì cộng đồng 2025 - Trung thu nghĩa tình 2025"
]

for activity in activities_2025:

    st.markdown(
        f'<div class="activity">{activity}</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<br>
<hr>

<div style="
    text-align:center;
    color:#888888;
    font-size:13px;
">
    CV Đặng Phú Hưng
</div>
""", unsafe_allow_html=True)


# ============================================================
# KẾT THÚC CV
# ============================================================

st.markdown('</div>', unsafe_allow_html=True)
